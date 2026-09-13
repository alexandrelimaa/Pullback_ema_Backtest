from report.grafics import plot
import pandas as pd

df = pd.read_parquet("../outputs/trades_baseline.parquet")
plot.equity_curve(df)
plot.drawdown_curve(df)
plot.profit_time_bars(df)
plot.profit_distribution(df)
plot.profit_weekday_bars(df)
plot.streak_loss_bar(df)

