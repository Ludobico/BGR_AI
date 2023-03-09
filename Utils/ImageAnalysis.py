import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-t",
                "--exercise_type",
                type=str,
                help='Type of activity to do',
                required=True)

args = vars(ap.parse_args())

print(args)
