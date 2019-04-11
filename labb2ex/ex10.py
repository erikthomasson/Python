

def find_and_replace(find_str, replace_str, infile, outfile):
    with open(infile, 'rt') as fin:
        with open(outfile, 'wt') as fout:
            for line in fin:
                fout.write(line.replace(find_str, replace_str))
