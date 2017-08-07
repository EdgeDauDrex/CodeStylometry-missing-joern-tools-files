
Gremlin.defineStep('functionToFeatureVec', [Vertex, Pipe], {
        _()
        .functionToASTNodes()
        .filter{it.type in ['IdentifierDeclType', 'ParameterType', 'Callee', 'Sizeof']}
	.code
});
