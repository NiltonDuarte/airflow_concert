from airflow.operators.dummy import DummyOperator

from airflow_concert.motif.motif_base import MotifBase


class EndMotif(MotifBase):
    def __init__(self, config, name=None) -> None:
        super().__init__(name=name, config=config)

    def build(self, dag, task_group):
        operator = DummyOperator(task_id=self.name, dag=dag, task_group=task_group)
        return operator
