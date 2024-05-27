import argparse
import json

from datasets import load_dataset

parser = argparse.ArgumentParser()
parser.add_argument(
    'output_dir',
    type=str,
    default='eval_data/instances',
    help='Path to the directory to save the instances.',
)
args = parser.parse_args()

dataset = load_dataset('princeton-nlp/SWE-bench')
test = dataset['test'].to_pandas()
test['PASS_TO_PASS'] = test['PASS_TO_PASS'].apply(json.loads)
test['FAIL_TO_PASS'] = test['FAIL_TO_PASS'].apply(json.loads)
test.to_json(f'{args.output_dir}/swe-bench-test.json', orient='records')

dataset = load_dataset('princeton-nlp/SWE-bench_Lite')
test = dataset['test'].to_pandas()
test['PASS_TO_PASS'] = test['PASS_TO_PASS'].apply(json.loads)
test['FAIL_TO_PASS'] = test['FAIL_TO_PASS'].apply(json.loads)
test.to_json(f'{args.output_dir}/swe-bench-test-lite.json', orient='records')
