# Getting FMS-DGT up and running

## clone the fms-dgt repo

```bash
git clone git@github.com:IBM/fms-dgt.git
cd fms-dgt
```

## Install dependencies

This includes venv creation + activation for dependency installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[all]"
```

## Update the `task.yaml` file

It's at: `MOSAIC/src/MOSAIC/models/transformer_model/fms-dgt/tasks/public/time_series/tinnitus/task.yaml`

## Run the task

```bash
python -m fms_dgt.public \
    --task-paths ./tasks/public/time_series/tinnitus/task.yaml
```

## Or run via slurm.sh file

```bash
sbatch slurm.sh
```

Then view if it's running by:

```bash
squeue
```

## Follow output files using `tail` (autoselect newest `.out` or `.err`)

```bash
tail -f "$(ls -t outputs/* | head -n 1)"
```

More info on tail command here: [tail command](../../MISC/tail_follow_latest_output_file.md)
