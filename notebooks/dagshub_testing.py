import dagshub
dagshub.init(repo_owner='Abas527', repo_name='mlops', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)