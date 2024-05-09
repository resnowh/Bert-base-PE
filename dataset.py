from datasets import load_dataset


def load_and_preprocess_dataset(tokenizer):
    # 加载训练集和验证集
    train_dataset = load_dataset('glue', 'mrpc', split='train')
    eval_dataset = load_dataset('glue', 'mrpc', split='validation')

    # 定义将文本编码成模型输入格式的函数
    def encode(examples):
        return tokenizer(examples['sentence1'], examples['sentence2'], truncation=True, padding='max_length')

    # 对数据集应用编码函数
    train_dataset = train_dataset.map(encode, batched=True)
    eval_dataset = eval_dataset.map(encode, batched=True)

    return {'train': train_dataset, 'eval': eval_dataset}