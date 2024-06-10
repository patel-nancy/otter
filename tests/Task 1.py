OK_FORMAT = True

test = {   'name': 'Task 1',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(simpleCircuit(), QuantumCircuit)\nTrue',
                                       'failure_message': 'EXPECTED FUNCTION TO RETURN TYPE QuantumCircuit',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1},
                                   {'code': '>>> simpleCircuit().num_clbits == 1\nTrue', 'failure_message': 'EXPECTED CIRCUIT TO HAVE 1 CLASSICAL BIT', 'hidden': False, 'locked': False, 'points': 1},
                                   {'code': '>>> simpleCircuit().num_qubits == 1\nTrue', 'failure_message': 'EXPECTED CIRCUIT TO HAVE 1 QUBIT', 'hidden': False, 'locked': False, 'points': 1},
                                   {   'code': '>>> def testMeasurementPerformedSimple():\n'
                                               '...     ops = simpleCircuit().count_ops()\n'
                                               "...     return ops['measure'] == 1 if 'measure' in ops else False\n"
                                               '>>> testMeasurementPerformedSimple()\n'
                                               'True',
                                       'failure_message': 'EXPECTED CIRCUIT TO PERFORM A MEASUREMENT',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1},
                                   {   'code': '>>> def testProbabilitiesSimple():\n'
                                               '...     qc = simpleCircuit()\n'
                                               "...     job = execute(qc, BasicAer.get_backend('statevector_simulator'), shots=1)\n"
                                               '...     return list(job.result().get_statevector(qc)) == [1, 0]\n'
                                               '>>> testProbabilitiesSimple()\n'
                                               'True',
                                       'failure_message': 'EXPECTED CIRCUIT TO PRODUCE STATE |0>',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1},
                                   {   'code': '>>> def testMeasurementPerformedSimple():\n'
                                               '...     ops = simpleCircuit().count_ops()\n'
                                               "...     return ops['measure'] == 1 if 'measure' in ops else False\n"
                                               '>>> \n'
                                               '>>> def testProbabilitiesSimple():\n'
                                               '...     qc = simpleCircuit()\n'
                                               "...     job = execute(qc, BasicAer.get_backend('statevector_simulator'), shots=1)\n"
                                               '...     return list(job.result().get_statevector(qc)) == [1, 0]\n'
                                               '>>> isinstance(simpleCircuit(), QuantumCircuit) and simpleCircuit().num_clbits == 1 and (simpleCircuit().num_qubits == 1) and '
                                               'testMeasurementPerformedSimple() and testProbabilitiesSimple()\n'
                                               'True',
                                       'failure_message': 'ONE OF THE ABOVE TESTS IS NOT PASSING',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 15}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
