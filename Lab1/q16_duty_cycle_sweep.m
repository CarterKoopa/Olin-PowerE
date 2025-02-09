conv_ratio = [];
mdl = plecs('get', '', 'CurrentCircuit');
v_scope = [mdl '/Scope2'];
constant_block = [mdl '/Constant']

duty_cycles = 10:10:90

for d = 1:length(duty_cycles)
	d_set = duty_cycles(d) / 100
	plecs('set', constant_block, 'Value', mat2str(d_set, 2))
	out = plecs('simulate');
	output = plecs('scope', v_scope, 'GetCursorData', [0.99e-2 1e-2]).cursorData{1}{1}.cursor2
	% mean_output = mean(cell2mat(struct2cell(output)))
	ratio = round(output) ./ 100;
	conv_ratio = [conv_ratio; d_set ratio]
end

csvwrite('q16_ratio_duty.csv', conv_ratio)