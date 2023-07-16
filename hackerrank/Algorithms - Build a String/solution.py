# https://www.hackerrank.com/challenges/build-a-string/problem?isFullScreen=true
# NOTE: this isn't actually complete. Hackerrank has some really stringent memory requirements.
# They can probably be met by precomputing substrings of interest on the target string and only keeping track
# of those, rather than all possible substrings.
def update_costs_dict(costs: dict, target_idx: int, cost: float):
    # Assign only known cost if none available
    if target_idx not in costs:
        costs[target_idx] = cost
    # Pick cheapest cost of options available
    costs[target_idx] = min(costs[target_idx], cost)


def build_string(a_cost, b_cost, target_str):
    costs = {0: a_cost}
    known_substrings = set()
    target_len = len(target_str)
    for current_idx in range(target_len):

        # Only for debugging purposes
        current_str = target_str[0:current_idx + 1]

        # Update known substrings
        for sub_str_idx in range(min(current_idx + 1, target_len)):
            sub_str = target_str[sub_str_idx: current_idx + 1]
            # Added as a memory-saving measure. No point in adding a substring larger than the remaining string.
            if len(sub_str) < target_len - current_idx:
                known_substrings.add(sub_str)

        # Case A: adding 1 character
        update_costs_dict(costs, min(target_len - 1, current_idx + 1), costs[current_idx] + a_cost)

        # Case B: adding a known substring
        for sub_str_idx in range(1, len(current_str) + 1):
            target_idx = min(current_idx + 1 + sub_str_idx, target_len)
            possible_substring = target_str[current_idx + 1: target_idx]
            if possible_substring in known_substrings:
                update_costs_dict(costs, target_idx - 1, costs[current_idx] + b_cost)

    return costs[target_len - 1]


# out = build_string(a_cost=4, b_cost=5, target_str='aabaacaba')
# print(out)
#
# out2 = build_string(a_cost=8, b_cost=9, target_str='bacbacacb')
# print(out2)

out3 = build_string(a_cost=8368, b_cost=8371,
                    target_str='abcabcajapkcdabcalajapkcdabckdabccojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbcajapkcdabcojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbajapkcdabckdabccojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbcajapkgpkcdabckdabccojasaajapkcdabcalajapkcdabckdabccojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbcajapkcdabcojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbajapkcdabckdabccojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbcajapkgpkcdabckdabccojkckcdabckdabccojerbcajapkcdabcojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbajapkcdabckdabccojccojasaajapkcdabcalajapkcdabckdabccojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbcajapkcdabcojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbajapkcdabckdabccojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbcajapakeoccojerbcajapkcdabcojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbajapkcdabckdabccojerbcajapkcdabcalpkcdabckdabccojerbcajapkcdabcalatrhajapkcdabcalajapfjacabcalatrhajapkcdabcalajapkcdabckdabccojerbcajapkgpkcdabckdabccojasaajapkcdabcalajapkcdabckdabccojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbcajapkcdabcojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbajapkcdabckdabccojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbcajapkgpkcdabckdabccojkckcdabckdabccojerbcajapkcdabcojerbcajapkcdabcalatrhajapkcdabcalajapkcdabckdabccojerbajapkcdabckdabccojccojasaajapjpdacabcabckdabccojerbajapkcdabckdabccojccojasaajapkcdabcalajapkcdabckdsmapkcdabsab')
print(out3)

out4 = build_string(a_cost=7233, b_cost=7234,
                    target_str='bccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigbccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbcctbccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigbccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcabbrngbgbccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbcctbccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigbccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsomcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigbccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbcctbccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigbccadbccagfdmpbccadbccagfmcsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaicsdfcidmpbccadbccagfmcsdfcgfmcsdfcidmpbccaigpmadbccagfdmpbccadbccagfmcsdfcidmpbccccagkcgfmcsdfcidmpbccaigpmahmfdhdc')
print(out4)

out5 = build_string(a_cost=636, b_cost=641,
                    target_str='baccbacaccbbaccbacccbacabaccqcbrqcacdnpsqcacdnpsccacdnpsccacdbrqcacdnbrqcacdeeahfrqcacgbbprqcbrqcacqqidnjrqcacdnedcbrqcbklrqcbrqqcacdnacdbrqrjmjklrrcacdnpsqcanoqidnjrqcacbkjmaccbagtdarqcacbkjbcacqcapgjoqrjmjklrdnedcbdnpsqcaoidnjrqdnpspmpodjrqcacbhrqcabdnacdiaccqcbkbspmpodjbsfemmcacccgdcbrqcbkliqcacqqishenhodjrqcacbhmpjgfemgpdkliqcacqqirspmpodjbeacgbbprqcbrndhaccbagtdrqdatmcacccarqcacbkdsmrimjqcapgjoqrjtccgdcbrigdcbrqcbkrjmjklraccbacgdcbrqcbkjfcacgaillmcbagtdacrjtccgajacdetdaracrjtccgaillmcbaagpsccacdbrblbthaccbagtdoijtdacbkjfsonrtnraccbanirbkstttjjdgtdacbkjfspmricnjdentgfnrpimkjmokkjbgnpsqpesntgfnrpimcacdbrblbtjntgfnrprqcbkrjmjkkstttjjdgteojbrndrgajntdrqdodablbthaccgidlrqqcacdnarkkipsccacdbrqpjfcacraccbqcbkliqckrejsajkmgsbeacgbbpqhijpmpodjrqcadsqpsccacdbracshrqnpsqcankenpodjrqcaqddmcbagtdsfjkenpoacdetgfnrpimcasmbtdjmcacpsqpesntgsqpesntgfnprqcfrpisntgfnprqdgtdcbbaccbhqppofondrgacbaccoqgacbrdhaccaobamcacqqishiaccqrqcbkllfbsonrtnracqnginleilrgacbacccbkjfspmriftgfnrpimfcacgaillmmpcacgaillmmaccbacgdctacdnacdbrqromsqpesntgfncbrqcbkjgiqqirspmpodsmiijpmpgrqcbklrehpthoqrqcbpodsctgajkmgsbeaqcbklicbbacccbkbbpbbfbrqcbkjgdbrqcbkjdrrkkipsdliqcqctdrqdbnrtcbasttqjdgfnrpimgmbadpdqodpqhbaccoqdtgfsnqcbkllfbsoeskeqjdgfnrpimfsnqcbkllbcacqcpqlrrdspeqcahaccbatdjmcachcdcbklrehptgsdoijtkdabdnqishiahaccighleblcaqfhjjrcdbrqrofqishiafidnjrqcatgfncbjrcbqcacbhmhanacdbrqqccacbhmpjhggtmcacccdgfbsonrsldcbrqhqcbrndpkrbsopdqodpqhbacbacsqqirspmpodamsbeaqcbklftadctaoqgacbrdhactpcsqqirspcbbacccbklkcshrtdksqqirspe')
print(out5)
