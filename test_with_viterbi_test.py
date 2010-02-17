def forward_viterbi(obs, states, start_p, trans_p, emit_p):
   T = {}
   for state in states:
       ##          prob.           V. path  V. prob.
       T[state] = (start_p[state], [state], start_p[state])
   for output in obs:
       U = {}
       for next_state in states:
           total = 0
           argmax = None
           valmax = 0
           for source_state in states:
               (prob, v_path, v_prob) = T[source_state]
               p = emit_p[source_state][output] * trans_p[source_state][next_state]
               prob *= p
               v_prob *= p
               total += prob
               if v_prob > valmax:
                   argmax = v_path + [next_state]
                   valmax = v_prob
           U[next_state] = (total, argmax, valmax)
       T = U
   ## apply sum/max to the final states:
   total = 0
   argmax = None
   valmax = 0

   #unnneeded comment here.
   
   for state in states:
       (prob, v_path, v_prob) = T[state]
       total += prob
       if v_prob > valmax:
           argmax = v_path
           valmax = v_prob
   return (total, argmax, valmax)


def example():
    states = ('Rainy', 'Sunny')

    observations = ('walk', 'shop', 'clean')
    observations = ('walk', 'shop', 'clean', 'shop', 'shop', 'shop', 'walk', 'walk', 'walk', 'walk')

    start_probability = {'Rainy': 0.6, 'Sunny': 0.4}

    transition_probability = {
        'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
        'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
        }

    emission_probability = {
        'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
        'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
        }

    unneeded_obj = { 'foo' }


    return forward_viterbi(observations,
                           states,
                           start_probability,
                           transition_probability,
                           emission_probability)
print example()
