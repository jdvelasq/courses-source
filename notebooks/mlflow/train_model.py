
# -----------------------------------------------------------------------------
# El código es identico al usado en los tutoriales anteriores
# -----------------------------------------------------------------------------


def load_data():

    import pandas as pd

    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    df = pd.read_csv(url, sep=";")

    y = df["quality"]
    x = df.copy()
    x.pop("quality")

    return x, y


def make_train_test_split(x, y):

    from sklearn.model_selection import train_test_split

    (x_train, x_test, y_train, y_test) = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=123456,
    )
    return x_train, x_test, y_train, y_test


def eval_metrics(y_true, y_pred):

    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    return mse, mae, r2


def report(estimator, mse, mae, r2):

    print(estimator, ":", sep="")
    print(f"  MSE: {mse}")
    print(f"  MAE: {mae}")
    print(f"  R2: {r2}")


def train_estimator(alphas, l1_ratios, n_splits=5, verbose=1):

    from sklearn.linear_model import ElasticNet
    from sklearn.model_selection import GridSearchCV

    import mlflow
    import mlflow.sklearn

    x, y = load_data()
    x_train, x_test, y_train, y_test = make_train_test_split(x, y)

    estimator = GridSearchCV(
        estimator=ElasticNet(
            random_state=12345,
        ),
        param_grid={
            "alpha": alphas,
            "l1_ratio": l1_ratios,
        },
        cv=n_splits,
        refit=True,
        verbose=0,
        return_train_score=False,
    )

    estimator.fit(x_train, y_train)

    estimator = estimator.best_estimator_

    mse, mae, r2 = eval_metrics(y_test, y_pred=estimator.predict(x_test))
    if verbose > 0:
        report(estimator, mse, mae, r2)

    with mlflow.start_run():

        params = estimator.get_params()

        mlflow.log_param("alpha", params["alpha"])
        mlflow.log_param("l1_ratio", params["l1_ratio"])
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        mlflow.sklearn.log_model(estimator, "model")


if __name__ == "__main__":

    import sys

    import numpy as np

    #
    # Ejemplo: python3 train_model.py 0.0001 0.5 10 0.0001 0.5 10
    #

    alpha_from = float(sys.argv[1])
    alpha_to = float(sys.argv[2])
    alpha_n = int(sys.argv[3])

    l1_ratio_from = float(sys.argv[4])
    l1_ratio_to = float(sys.argv[5])
    l1_ratio_n = int(sys.argv[6])

    train_estimator(
        alphas=np.linspace(
            alpha_from,
            alpha_to,
            alpha_n,
        ),
        l1_ratios=np.linspace(
            l1_ratio_from,
            l1_ratio_to,
            l1_ratio_n,
        ),
        n_splits=5,
        verbose=1,
    )
