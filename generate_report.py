import matplotlib.pyplot as plt

def parse_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        if ':' in line:
            timestamp, info = line.strip().split(':', 1)
            district, city, weapon, origin = info.split('   ')
            data[timestamp] = [district, city, weapon, origin]
    
    return data

def create_bar_chart(data, output_path):
    shots_per_city = {}
    for value in data.values():
        if value[0].lower() == "haifa":
            if value[1] not in shots_per_city:
                shots_per_city[value[1]] = 0
            shots_per_city[value[1]] += 1
    
    plt.figure(figsize=(10,6))
    plt.bar(shots_per_city.keys(), shots_per_city.values(), color ='skyblue')
    plt.title('Daily Report')
    plt.xlabel('City')
    plt.ylabel('Number of Events')
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()

def main():
    text_file_path = 'data.txt'
    chart_output_path = 'chart.png'

    data = parse_text_file(text_file_path)
    create_bar_chart(data, chart_output_path)
    print("Report created")

if __name__ == "__main__":
    main()
    

