class Dataloader(object):
    def __init__(self, dataset, batch_size):
        self.dataset = dataset
        self.batch_size = batch_size
        # self.size = len(dataset)

    def __getitem__(self, i):
        print(i)
        # start = i * self.batch_size
        # stop = (i + 1) * self.batch_size
        # batch_data = []
        # for j in range(start, stop):
        #     batch_data.append(self.dataset[j])

        # return batch_data

    # def __len__(self):
    #     return self.size // self.batch_size

if __name__ == "__main__":
    dataset = [i for i in range(1,105)]
    batch_size = 10
    train_data = Dataloader(dataset, batch_size)
    print(type(train_data))
    print(train_data[10])
    # for e in train_data:
    #     print(type(e), e)
