def solution(id_list, report, k):
    report_list = {}
    
    for r in report :
       	if r.split()[1] not in report_list.keys() :
            report_list[r.split()[1]] = []
        if r.split()[0] not in report_list[r.split()[1]] :
            report_list[r.split()[1]].append(r.split()[0])
    
    report_id = [0 for i in id_list]
    
    for i in report_list :
        if len(report_list[i]) >= k :
            for j in report_list[i] :
                report_id[id_list.index(j)] += 1 
    
    return report_id