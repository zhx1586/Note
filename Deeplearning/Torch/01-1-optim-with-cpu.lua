require 'cutorch'

-- 1 定义正定二次型 J(x)
torch.manualSeed(1234);
N = 5;
A = torch.rand(N, N)
-- print(A)
A = A*A:t()
-- print(A)
A:add(0.001, torch.eye(N))
b = torch.rand(N)

-- x: N*1
-- A: N*N
-- b: N*1
function J(x)
	return 0.5*x:dot(A*x)-b:dot(x)
end
-- print(J(torch.rand(N)))

-- 2 使用解析法求解最小值
xs = torch.inverse(A)*b
print(string.format('J(x^*)=%g', J(xs)))

-- 3 使用梯度下降法求解最小值

-- x: N*1
-- A: N*N
-- b: N*1
function dJ(x)
	return A*x-b
end

--[[
x = torch.rand(N) -- 解的初始值
lr = 0.01 -- 学习速率
for i=1,20000 do
	x = x - dJ(x)*lr
	print(string.format('at iter %d J(x)=%f', i, J(x)))
end
--]]

-- 4 使用 optim包

-- 更好的梯度函数定义方式
--[[
do
	local neval = 0
	function JdJ(x)
		local Jx = J(x)
		neval = neval + 1
		print(string.format('after %d evaluations J(x)=%f', neval, Jx))
		return Jx, dJ(x)
	end
end

require 'optim'

state = {verbose = true, maxIter = 100} -- cg法
x = torch.rand(N)
optim.cg(JdJ, x, state)
--]]

require 'optim'

-- cg法
evaluations = {}
time = {}
timer = torch.Timer()
neval = 0
function JdJ(x)
	local Jx = J(x)
	neval = neval + 1
	print(string.format('after %d evaluations J(x)=%f', neval, Jx))
	table.insert(evaluations, Jx)
	table.insert(time, timer:time().real)
	return Jx, dJ(x)
end

state = {verbose = true, maxIter = 100}
x0 = torch.rand(N)
cgx = x0:clone()
timer:reset()
optim.cg(JdJ, cgx, state)

cgtime = torch.Tensor(time)
cgevaluations = torch.Tensor(evaluations)

-- sgd法
evaluations = {}
time = {}
neval = 0

state = {lr = 0.01}
sgdx = x0:clone()
timer:reset()

for i = 1,200000 do
	optim.sgd(JdJ, sgdx, state)
end

sgdtime = torch.Tensor(time)
sgdevaluations = torch.Tensor(evaluations)

-- 5 绘图
require 'gnuplot'

gnuplot.figure(1)
gnuplot.title('cg loss')
gnuplot.plot(cgtime, cgevaluations)

gnuplot.figure(2)
gnuplot.title('sgd loss')
gnuplot.plot(sgdtime, sgdevaluations)