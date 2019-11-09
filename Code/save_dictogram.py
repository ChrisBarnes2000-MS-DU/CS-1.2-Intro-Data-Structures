def save_to_file(self, histogram_as_dict, filename):
        with open(filename, 'w+') as f:
            for key, value in histogram_as_dict.items():
                f.write("{}\t{}\n".format(key, value))
