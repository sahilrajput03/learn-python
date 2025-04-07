import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
import numpy as np


# Simple tokenizer for our very limited vocabulary
class SimpleTokenizer:
    def __init__(self):
        self.vocab = {"<PAD>": 0, "Hello": 1, ",": 2, "World": 3, "!": 4}
        self.id_to_token = {v: k for k, v in self.vocab.items()}
        self.vocab_size = len(self.vocab)

    def encode(self, text):
        return [self.vocab[token] for token in text.split()]

    def decode(self, ids):
        return " ".join([self.id_to_token[id] for id in ids])


# Dataset for "Hello, World!"
class HelloWorldDataset(Dataset):
    def __init__(self, tokenizer, samples=1000):
        self.tokenizer = tokenizer
        self.samples = samples
        self.input_seq = self.tokenizer.encode("Hello ,")
        self.target_seq = self.tokenizer.encode("World !")

    def __len__(self):
        return self.samples

    def __getitem__(self, idx):
        return {
            "input": torch.tensor(self.input_seq, dtype=torch.long),
            "target": torch.tensor(self.target_seq, dtype=torch.long),
        }


# Simple Transformer-like model
class TinyLLM(nn.Module):
    def __init__(self, vocab_size, d_model=32, nhead=2, num_layers=2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.transformer = nn.Transformer(
            d_model=d_model,
            nhead=nhead,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            batch_first=True,
        )
        self.fc_out = nn.Linear(d_model, vocab_size)

    def forward(self, src, tgt):
        src_emb = self.embedding(src)
        tgt_emb = self.embedding(tgt)

        # Create masks for transformer
        src_mask = torch.zeros((src.size(1), src.size(1)), device=src.device).bool()
        tgt_mask = nn.Transformer.generate_square_subsequent_mask(tgt.size(1)).to(
            tgt.device
        )

        output = self.transformer(
            src_emb, tgt_emb, src_mask=src_mask, tgt_mask=tgt_mask
        )

        return self.fc_out(output)


# Training function
def train_hello_world_llm():
    # Initialize tokenizer and dataset
    tokenizer = SimpleTokenizer()
    dataset = HelloWorldDataset(tokenizer)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    # Initialize model
    model = TinyLLM(tokenizer.vocab_size)

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    epochs = 20
    for epoch in range(epochs):
        total_loss = 0
        for batch in dataloader:
            optimizer.zero_grad()

            input_seq = batch["input"]
            target_seq = batch["target"]

            # For transformer input, we need a "shifted" target
            tgt_input = torch.cat(
                [
                    torch.zeros((target_seq.size(0), 1), dtype=torch.long),
                    target_seq[:, :-1],
                ],
                dim=1,
            )

            # Forward pass
            output = model(input_seq, tgt_input)

            # Reshape output for loss calculation
            output = output.view(-1, tokenizer.vocab_size)
            target = target_seq.reshape(-1)

            # Calculate loss
            loss = criterion(output, target)

            # Backward pass
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        # Print epoch stats
        if (epoch + 1) % 5 == 0:
            print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(dataloader):.4f}")

    # Test the model
    model.eval()
    with torch.no_grad():
        input_seq = torch.tensor([tokenizer.encode("Hello ,")], dtype=torch.long)
        target_start = torch.zeros((1, 1), dtype=torch.long)

        # Generate output tokens one by one
        generated = []
        for _ in range(2):  # We expect 2 tokens: "World" and "!"
            tgt_input = torch.cat(
                [target_start] + [torch.tensor([[token]]) for token in generated], dim=1
            )
            output = model(input_seq, tgt_input)
            next_token = output[0, -1].argmax().item()
            generated.append(next_token)

        print(f"Input: {tokenizer.decode(input_seq[0].tolist())}")
        print(f"Generated: {tokenizer.decode(generated)}")
        # & Expected Output:
        #       Input: Hello ,
        #       Generated: World !


if __name__ == "__main__":
    train_hello_world_llm()
