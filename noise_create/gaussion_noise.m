clear;
N = 2000;
T = 0.005;

sigma_v = 6.9906*10^(-6);   %陀螺漂移噪声的方差
sigma_n = 1.4142*10^(-9);   %陀螺状态噪声和量测噪声的方差
sigma_x = 1*10^(-5);        %星敏感器状态噪声的方差
sigma_z = 1*10^(-12);       %星敏感器量测噪声的方差

g_x=randn(3,N)*sigma_n;   %陀螺状态噪声，均值为0，方差为sigma_n
g_z=randn(3,N)*sigma_n;   %陀螺量测噪声噪声，均值为0，方差为sigma_n
v = randn(3,N)*sigma_v;   %陀螺漂移噪声

s_x=randn(4,N)*sigma_x;     %星敏感器状态噪声，均值为0，方差为sigma
s_z=randn(4,N)*sigma_z;     %星敏感器量测噪声，均值为0，方差为sigma

X_star(:,1)=[1 0 0 0]';   %星敏感器理想值
X_gyro(:,1)=[0 0 0]';     %陀螺理想值

gyro_drift = 0;           %陀螺漂移初值
for t=2:N
    X_star(:,t) = X_star(:,t-1);
    X_gyro(:,t) = X_gyro(:,t-1);
end
for i=1:N
    gyro_drift = gyro_drift+T*v(:,i);           %陀螺漂移积分
    X_star_noise(:,i) = X_star(:,i)+s_x(:,i);   %模拟实际姿态角
    Z_star(:,i) = X_star_noise(:,i)+s_z(:,i);   %模拟量测姿态角
    X_gyro_noise(:,i) = X_gyro(:,i)+g_x(:,i);   %模拟实际姿态角速度
    Z_gyro(:,i) = X_gyro_noise(:,i)+g_z(:,i)+gyro_drift;   %模拟量测姿态角速度  
end

figure;
% plot(Z_star(1,:),'b')
% hold on;
plot(Z_star(2,:),'r')
hold on;
plot(Z_star(3,:),'y')
hold on;
plot(Z_star(4,:),'c')
hold on;
title('star');
legend()

figure;
plot(Z_gyro(1,:),'b')
hold on;
plot(Z_gyro(2,:),'r')
hold on;
plot(Z_gyro(3,:),'y')
hold on;
title('gyro');
legend()
