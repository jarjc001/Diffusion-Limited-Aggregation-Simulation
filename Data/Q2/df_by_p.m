Data = csvread('df_p.csv',1,0);
%reads csv file called "test results" and makes a 2D Matrix called Data

 start_point = 1;
 end_point = 12;


p = Data(start_point:end_point,1);
df = Data(start_point:end_point,2);
error = Data(start_point:end_point,3);
ln_p = Data(start_point:end_point,4);
ln_df = Data(start_point:end_point,5);
ln_error = Data(start_point:end_point,6);
m_ = Data(1,7);
c_ = Data(2,7);


lnRmean_space_ = linspace(-3, 1, 100);

map_lnNa_ = (m_*lnRmean_space_) + c_;

%sizeboi = size(lnRmean_);

%zero_ = zeros(sizeboi);


%lnNc/lnr grapth one iwth mean one with shown cluster
plot(ln_p,ln_df,'r^')
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
% 
% histogram(grad_,100);
