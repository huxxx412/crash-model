from jsonschema import validate
import json
import os
import subprocess
import shutil
from .. import make_preds_final

def test_make_preds_final_boston(tmpdir):
    """
    Confirm that final predictions generated conform to the schema
    """
    
    # Copy test data into temp directory in appropriate place
    test_data_path = os.path.dirname(
        os.path.abspath(__file__)) + "/data/boston_final_preds"

    tmpdir_data_path = tmpdir.strpath + "/data"
    shutil.copytree(test_data_path, tmpdir_data_path)

    # Call make_preds_final
    subprocess.check_call([
        "python",
        "-m",
        "data.make_preds_final",
        "-f",
        tmpdir_data_path
    ])

    with open(tmpdir_data_path + "/processed/preds_final.json") as f:
        test_preds_final = json.load(f)

    # verify schema of output file generated
    validate(test_preds_final, json.load(open(
        os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
                     "standards", "predictions-schema.json"))))