# from math import log

def viterbi(obs, states, start_p, trans_p, emit_p):
    v = [{}]

    for st in states:
        v[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}

    for t in range(1, len(obs)):
        v.append({})
        for st in states:
            max_tr_prob = v[t - 1][states[0]]["prob"] * trans_p[states[0]][st] * emit_p[st][obs[t]]
            prev_st_selected = states[0]
            for prev_st in states[1:]:
                tr_prob = v[t - 1][prev_st]["prob"] * trans_p[prev_st][st] * emit_p[st][obs[t]]
                if tr_prob > max_tr_prob:
                    max_tr_prob = tr_prob
                    prev_st_selected = prev_st

            max_prob = max_tr_prob
            v[t][st] = {"prob": max_prob, "prev": prev_st_selected}
            print(v, "\n")

    opt = []
    max_prob = 0.0
    best_st = None
    # Get most probable state and its backtrack
    for st, data in v[-1].items():
        if data["prob"] > max_prob:
            max_prob = data["prob"]
            best_st = st
    opt.append(best_st)
    previous = best_st

    for t in range(len(v) - 2, -1, -1):
        opt.insert(0, v[t + 1][previous]["prev"])
        previous = v[t + 1][previous]["prev"]

    return opt


observations = ('G', 'G', 'C', 'T')
hidden_states = ('a', 'b')

# start_probability = {'a': log10(0.5), 'b': log10(0.5)}
# transition_probability = {'a': {'a': log10(0.9), 'b': log10(0.1)},
#                           'b': {'a': log10(0.1), 'b': log10(0.9)}}
# emission_probability = {'a': {'A': log10(0.4), 'G': log10(0.4), 'C': log10(0.1), 'T': log10(0.1)},
#                         'b': {'A': log10(0.2), 'G': log10(0.2), 'C': log10(0.3), 'T': log10(0.3)}}

start_probability = {'a': 0.5, 'b': 0.5}
transition_probability = {'a': {'a': 0.9, 'b': 0.1},
                          'b': {'a': 0.1, 'b': 0.9}}
emission_probability = {'a': {'A': 0.4, 'G': 0.4, 'C': 0.1, 'T': 0.1},
                        'b': {'A': 0.2, 'G': 0.2, 'C': 0.3, 'T': 0.3}}

result = viterbi(observations, hidden_states, start_probability, transition_probability, emission_probability)
print(f'result: {result}')
