from math import ceil
def solution(fees, records):
    default_time = fees[0]
    default_fee = fees[1]
    added_time = fees[2]
    added_fee = fees[3]
    parking = {}
    parking_fee = {}
    cars = set([record.split()[1] for record in records])
    
    for car in cars :
        parking[car] = [record for record in records if car in record]
        if 'IN' in parking[car][-1] :
            parking[car].append(' '.join(['23:59', car, 'OUT']))
        # calculate fee
        time_sum = 0
        park = parking[car]
        for i in range (0, len(park), 2) :
            time_in = park[i].split()[0]
            time_out = park[i+1].split()[0]
            print("car :", car, time_in, time_out)
            time = (int(time_out.split(':')[0]) - int(time_in.split(':')[0])) * 60 + (int(time_out.split(':')[1]) - int(time_in.split(':')[1]))
            time_sum += time
            print(car, time_sum)
        
        if time_sum <= default_time :
            parking_fee[car] = default_fee
        else :
            parking_fee[car] = default_fee + ceil((time_sum - default_time) / added_time) * added_fee
    
    return [i[1] for i in sorted(parking_fee.items(), key=lambda x : x[0])]