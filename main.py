import pandas as pd

def run():
    df = pd.read_csv('input/pending_actions.csv', index_col=0, usecols=[1,2,3,9,10,11,12])

    print("Results:\n##########")

    _analyze_move_actions(df)
    _analyze_resize_actions(df)


def _analyze_move_actions(df):
    print(f"\tMove:")

    # selecting rows based on condition
    rslt_df = df[df['Action Type'] == 'Move']
    uniq_count = rslt_df.count()['Entity']
    print(f"\t\tVirtual Machines: {uniq_count}")

def _analyze_resize_actions(df):
    print(f"\tResize:")

    # selecting rows based on condition
    rslt_df = df[df['Action Type'] == 'Resize']
    print(rslt_df)
    uniq_count = rslt_df.count()['Entity']
    print(f"\t\tTotal Virtual Machines: {uniq_count}")

    # Extract the vCPU
    rslt_df_vcpu = rslt_df[rslt_df['Resource'] == 'VCPU']
    vcpu_uniq_count = rslt_df_vcpu['to'].sum()

    print(f"\t\t\tvCPU: {vcpu_uniq_count}")
    print(f"\t\t\tvMEM: ")
    print(f"\t\t\tCPU: ")
    print(f"\t\t\tMEM: ")


if __name__ == "__main__":
    run()
