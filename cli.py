import argparse
from diabetes.params import Params
from diabetes import nodes
from diabetes.reader import read_data

parser = argparse.ArgumentParser(description="Score diabetes model")
parser.add_argument(
    "--input-data", dest="input_data", help="input file to score the model"
)
parser.add_argument(
    "--output-data", dest="output_data", help="output file save the scored model"
)


def score_model(input_file, output_file):
    data = read_data(input_file)
    params = Params(input_file, output_file)
    data = nodes.data_prep.run(params, data)
    data = nodes.model_score.run(params, data)
    data = nodes.model_cutpoint.run(params, data)
    data.to_csv(output_file, index=False)


args = parser.parse_args()
input_file = args.input_data
output_file = args.output_data
if input_file is None or output_file is None:
    raise Exception("Cannot run pipeline without `--input-data` and `--output-data`")
score_model(input_file, output_file)
