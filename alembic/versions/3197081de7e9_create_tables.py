"""create tables

Revision ID: 3197081de7e9
Revises: 
Create Date: 2023-08-24 02:02:15.588022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from api.config.database import Database


# revision identifiers, used by Alembic.
revision: str = '3197081de7e9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    database = Database()

    # Criando tabela de trabalhadores
    database.get_engine().connect().execute(
        sa.text(
            "CREATE TABLE IF NOT EXISTS `worker` ( "
            "   `id` INT NOT NULL AUTO_INCREMENT , "
            "   `name` VARCHAR(255) NOT NULL , "
            "   `charge` FLOAT NOT NULL , "
            "   PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB;"
        )
    )

    # Criando tabela de Lojas
    database.get_engine().connect().execute(
        sa.text(
            "CREATE TABLE IF NOT EXISTS `zax_db`.`store` ( "
            "   `id` INT NOT NULL AUTO_INCREMENT , "
            "   `name` VARCHAR(255) NOT NULL , "
            "   `bonus_payment` FLOAT NOT NULL , "
            "   PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB;"
        )
    )

    # Criando tabela de trabalhadores que trabalham exclusivamente para algumas lojas
    database.get_engine().connect().execute(
        sa.text(
            "CREATE TABLE IF NOT EXISTS `zax_db`.`store_exclusive_worker` ( "
            "   `id` INT NOT NULL AUTO_INCREMENT, "
            "   `worker_id` INT NOT NULL, "
            "   `store_id` INT NOT NULL, "
            "   PRIMARY KEY (`id`), "
            "   FOREIGN KEY (`worker_id`)"
            "       REFERENCES `worker`(`id`)"
            "       ON DELETE CASCADE,"
            "   FOREIGN KEY (`store_id`)"
            "       REFERENCES `store`(`id`)"
            "       ON DELETE CASCADE"
            ") ENGINE=InnoDB;"
        )
    )

    # Criando tabela de ordem de pedidos
    database.get_engine().connect().execute(
        sa.text(
            "CREATE TABLE IF NOT EXISTS `zax_db`.`order` ( "
            "    `id` INT NOT NULL AUTO_INCREMENT ,"
            "    `store_id` INT NOT NULL ,"
            "    `price` FLOAT NOT NULL ,"
            "    `create_time` DATETIME NOT NULL ,"
            "    `worker_id` INT NULL ,"
            "    PRIMARY KEY (`id`),"
            "    FOREIGN KEY (`worker_id`) REFERENCES `worker`(`id`), "
            "    FOREIGN KEY (`store_id`) REFERENCES `store`(`id`)"
            ") ENGINE=InnoDB;"
        )
    )

def downgrade() -> None:
    database = Database()
    database.get_engine().connect().execute(sa.text("DROP TABLE `store_exclusive_worker`;"))
    database.get_engine().connect().execute(sa.text("DROP TABLE `order`;"))
    database.get_engine().connect().execute(sa.text("DROP TABLE `worker`;"))
    database.get_engine().connect().execute(sa.text("DROP TABLE `store`;"))
