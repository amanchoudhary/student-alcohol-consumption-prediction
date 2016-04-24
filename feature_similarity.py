from numpy import corrcoef

def get_feature(feature, index):
    result = []
    for row in feature:
        result.append(row[index])
    return result


def feature_correlation(feature):
    feature_list = []
    i = 0
    while i < len(feature[0]):
        feature_list.append(get_feature(feature, i))
        i += 1

    i = 0
    j = 0
    for i in range(0, len(feature_list)):
        for j in range(i+1, len(feature_list)):
            print i, j, max(corrcoef(feature_list[i], feature_list[j])[0][1], corrcoef(feature_list[j], feature_list[i])[0][1])

