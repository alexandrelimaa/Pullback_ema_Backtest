import pandas as pd
import helpers as h



df_trades = pd.read_parquet("outputs/trades_baseline.parquet")
tick_data_teste = h.clean_data(h.load_data('data/ticks/tick_2026-08-18.csv'))
tick_data_teste = tick_data_teste.sort_index()

teste_entry = 169720.0
trailing_activation = 65
teste_ticks = tick_data_teste.loc['2026-08-18 10:00:00':'2026-08-18 10:08:00']  # ajusta o horário pra cobrir a janela do trade
best_price = teste_ticks['Price'].cummax()
trailing_on = best_price <= (teste_entry - trailing_activation)
print(trailing_on.value_counts())

grupo = tick_data_teste[tick_data_teste.index == '2026-08-18 09:02:56']
print(grupo[['Price', 'Quantity']])