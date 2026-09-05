class SampleClass:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

sample_object = SampleClass(title="This is a sample class")

print(sample_object.title)
print(sample_object.done)

sample_object.done = True

print(sample_object.done)