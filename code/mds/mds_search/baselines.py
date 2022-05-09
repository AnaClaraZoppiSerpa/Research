example_baseline = {
    "id": "example_baseline",
    "xor_enc": 0,
    "xtime_enc": 0,
    "xor_dec": 0,
    "xtime_dec": 0,
    "xor_sum": 0,
    "xtime_sum": 0
}

hierocrypt_L1_2x2 = {
    "id": "hierocrypt_L1_2x2",
    "xor_enc": 8,
    "xtime_enc": 10,
    "xor_dec": 7,
    "xtime_dec": 11,
    "xor_sum": 8+7,
    "xtime_sum": 10+11
}

curupira_3x3_cheapest = {
    "id": "curupira_3x3_cheapest",
    "xor_enc": 12,
    "xtime_enc": 15,
    "xor_dec": 12,
    "xtime_dec": 15,
    "xor_sum": 12+12,
    "xtime_sum": 15+15
}

photon_5x5 = {
    "id": "photon_5x5",
    "xor_enc": 44,
    "xtime_enc": 52,
    "xor_dec": 44,
    "xtime_dec": 52,
    "xor_sum": 44+44,
    "xtime_sum": 52+52
}

photon_6x6 = {
    "id": "photon_6x6",
    "xor_enc": 59,
    "xtime_enc": 74,
    "xor_dec": 59,
    "xtime_dec": 74,
    "xor_sum": 59+59,
    "xtime_sum": 74+74
}

baselines = [photon_6x6]

def compare_to_baselines(xor_enc, xtime_enc, xor_dec, xtime_dec, xor_sum, xtime_sum):
    message = ""
    for baseline in baselines:
        message += "\n===================================\n"
        message += "Comparing to " + baseline['id'] + "\n"
        if xor_enc < baseline['xor_enc']:
            message += "- beats xor_enc: " + str(xor_enc) + " vs " + str(baseline['xor_enc']) + "\n"
        if xor_dec < baseline['xor_dec']:
            message += "- beats xor_dec: " + str(xor_dec) + " vs " + str(baseline['xor_dec']) + "\n"
        if xtime_enc < baseline['xtime_enc']:
            message += "- beats xtime_enc: " + str(xtime_enc) + " vs " + str(baseline['xtime_enc']) + "\n"
        if xtime_dec < baseline['xtime_dec']:
            message += "- beats xtime_dec: " + str(xtime_dec) + " vs " + str(baseline['xtime_dec']) + "\n"
        if xor_sum < baseline['xor_sum']:
            message += "- beats xor_sum: " + str(xor_sum) + " vs " + str(baseline['xor_sum']) + "\n"
        if xtime_sum < baseline['xtime_sum']:
            message += "- beats xtime_sum: " + str(xtime_sum) + " vs " + str(baseline['xtime_sum']) + "\n"
    return message
