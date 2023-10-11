from sqlalchemy import DECIMAL, Column, ForeignKey, Integer, MetaData, String, Table

metadata = MetaData()


invoices = Table(
    "invoices",
    metadata,
    Column("id", primary_key=True),
    Column("title", String),
    Column("discount", DECIMAL(precision=2)),
)


invoice_lines = Table(
    "invoice_lines",
    metadata,
    Column("id", primary_key=True),
    Column("title", String),
    Column("quantity", Integer),
    Column("price_per_one", DECIMAL(precision=2)),
    Column("invoice_id", ForeignKey("invoices.id", nullable=False)),
)
