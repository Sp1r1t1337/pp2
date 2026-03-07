import re
import json

def parse_receipt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
      
    date_time_match = re.search(r'(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})', content)
    date = date_time_match.group(1) if date_time_match else None
    time = date_time_match.group(2) if date_time_match else None

    payment_match = re.search(r'Банковская карта:', content)
    payment_method = "Bank Card" if payment_match else "Cash"

    product_pattern = re.compile(
        r'\d+\.\n(.*?)\n(?:\)?(\d+,\d+) x ([\d\s,]+\.\d{2})\n([\d\s,]+\.\d{2})', 
        re.DOTALL
    )
    
    items = []
    matches = product_pattern.findall(content)
    
    for match in matches:
        name = match[0].replace('\n', ' ').strip()
        quantity = float(match[1].replace(',', '.'))
        unit_price = float(match[2].replace(' ', '').replace(',', '.'))
        line_total = float(match[3].replace(' ', '').replace(',', '.'))
        
        items.append({
            "product_name": name,
            "quantity": quantity,
            "unit_price": unit_price,
            "line_total": line_total
        })

    total_match = re.search(r'ИТОГО:\n([\d\s,]+\.\d{2})', content)
    total_amount = float(total_match.group(1).replace(' ', '').replace(',', '.')) if total_match else 0.0

    receipt_data = {
        "metadata": {
            "date": date,
            "time": time,
            "payment_method": payment_method,
            "currency": "KZT"
        },
        "items": items,
        "total_amount": total_amount
    }
    
    return receipt_data

if __name__ == "__main__":
    data = parse_receipt('raw.txt')
    print(json.dumps(data, indent=4, ensure_ascii=False))
