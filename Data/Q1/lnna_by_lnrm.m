Data = csvread('3000_mean.csv',1,0);
%reads csv file called "test results" and makes a 2D Matrix called Data

start_point = 2;
end_point = 11;

lnRmean_space_ = linspace(2, 5, 100);
m_ = Data(31,11);
plusc_ = Data(1,11);

map_lnNa_ = (m_*lnRmean_space_) + plusc_;

N_ = Data(start_point:end_point,1);
Rm_ = Data(start_point:end_point,2);
Rmean_ = Data(start_point:end_point,3);
Rsd_ = Data(start_point:end_point,4);
lnNa_ = Data(start_point:end_point,5);
lnRm_ = Data(start_point:end_point,6);
lnRmean_ = Data(start_point:end_point,7);
lnRsd_ = Data(start_point:end_point,8);
grad_ = Data(start_point:end_point,11);

sizeboi = size(lnRmean_);

zero_ = zeros(sizeboi);


%lnNc/lnr grapth one iwth mean one with shown cluster
%plot(lnRm_,lnNa_,'r^',lnRmean_space_ ,map_lnNa_ ,'-.k')
%,lnRmean_,lnNa_,'k*'
%hold on 
%errorbar(lnRmean_,lnNa_,lnRsd_,'Horizontal')
% errorbar(lnRm_,lnNa_,zero_,'*^')
% errorbar(lnRmean_,lnNa_,lnRsd_,'^*');
% errorbar(lnRmean_space_ ,map_lnNa_ ,zero_,'-.k');

% legend({'cos(x)','cos(2x)','cos(3x)'},...
%     'Location','northwest','NumColumns',1)
% 
% 
% xlim([2.5 4.7])
% ylim([4.5 8.1])
% xlabel('ln r_m_a_x')
% ylabel('ln N_c')
% 
% 

histogram(grad_,100);
