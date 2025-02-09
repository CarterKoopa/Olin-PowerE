conv_ratio = [];
mdl = plecs('get', '', 'CurrentCircuit');
v_scope = [mdl '/Scope3'];
inductor = [mdl '/L1']

for L = 1:15
	L_set = L * 1e-6
	plecs('set', inductor, 'L', mat2str(L_set, 5))
	out = plecs('simulate');
	output = plecs('scope', v_scope, 'GetCursorData', [0.2e-2 0.8e-2]).cursorData{1}{1}.cursor1;
	ratio = output ./ 100;
	conv_ratio = [conv_ratio; L_set ratio]
end

csvwrite('q12_ratio_inductance.csv', conv_ratio)