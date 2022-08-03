text = " Какой- то текст"

unique_symbol = set(text)
for symbol in unique_symbol:
     symbol_count = text.count(symbol)
     print(f"'{symbol}' - {symbol_count}")