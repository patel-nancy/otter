OK_FORMAT = True

test = {   'name': 'Task 5',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(opposites(), QuantumCircuit)\nTrue',
                                       'failure_message': 'EXPECTED FUNCTION TO RETURN TYPE QuantumCircuit',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1},
                                   {'code': '>>> opposites().num_clbits == 2\nTrue', 'failure_message': 'EXPECTED CIRCUIT TO HAVE 2 CLASSICAL BITS', 'hidden': False, 'locked': False, 'points': 1},
                                   {'code': '>>> opposites().num_qubits == 2\nTrue', 'failure_message': 'EXPECTED CIRCUIT TO HAVE 2 QUBITS', 'hidden': False, 'locked': False, 'points': 1},
                                   {   'code': ">>> def testNoInitialize():\n...     ops = opposites().count_ops()\n...     return 'initialize' not in ops\n>>> testNoInitialize()\nTrue",
                                       'failure_message': 'CIRCUIT SHOULD NOT USE INITIALIZE',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1},
                                   {   'code': '>>> def testRequirementsOpposites():\n'
                                               '...     ops = opposites().count_ops()\n'
                                               "...     if 'measure' not in ops:\n"
                                               '...         return False\n'
                                               "...     x = 'x' in ops and ops['x'] == 1\n"
                                               "...     return ops['measure'] == 2 and x\n"
                                               '>>> testRequirementsOpposites()\n'
                                               'True',
                                       'failure_message': 'CIRCUIT SHOULD MEASURE EACH QUBIT TO ITS CORRESPONDING CLASSICAL BIT',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1},
                                   {   'code': '>>> def testProbabilitiesOpposites():\n'
                                               '...     qc = opposites().reverse_bits()\n'
                                               "...     job = execute(qc, BasicAer.get_backend('statevector_simulator'), shots=10)\n"
                                               '...     return list(job.result().get_statevector(qc)) == [0, 1, 0, 0]\n'
                                               '>>> testProbabilitiesOpposites()\n'
                                               'True',
                                       'failure_message': 'Measured unexpected state.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1},
                                   {   'code': '>>> def testNoInitialize():\n'
                                               '...     ops = opposites().count_ops()\n'
                                               "...     return 'initialize' not in ops\n"
                                               '>>> \n'
                                               '>>> def testProbabilitiesOpposites():\n'
                                               '...     qc = opposites().reverse_bits()\n'
                                               "...     job = execute(qc, BasicAer.get_backend('statevector_simulator'), shots=10)\n"
                                               '...     return list(job.result().get_statevector(qc)) == [0, 1, 0, 0]\n'
                                               '>>> \n'
                                               '>>> def testRequirementsOpposites():\n'
                                               '...     ops = opposites().count_ops()\n'
                                               "...     if 'measure' not in ops:\n"
                                               '...         return False\n'
                                               "...     x = 'x' in ops and ops['x'] == 1\n"
                                               "...     return ops['measure'] == 2 and x\n"
                                               '>>> isinstance(opposites(), QuantumCircuit) and opposites().num_clbits == 2 and (opposites().num_qubits == 2) and testNoInitialize() and '
                                               'testRequirementsOpposites() and testProbabilitiesOpposites()\n'
                                               'True',
                                       'failure_message': 'ONE OF THE ABOVE TESTS IS NOT PASSING',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 9}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
