%ªÊÕº
clc;
close all;

%‘ÿ»Î ˝æ›
data = load('data.txt');
[N,M] = size(data);
t = data(:,1);
roll = data(:,2:3);
yaw = data(:,4:5);
pitch = data(:,6:7);


%ªÊÕº
%roll
figure(1);
plot(t, roll(1:N,1),'.-');
hold on;grid on;
plot(t, roll(1:N,2),'.-');
xlabel('t/s');
ylabel('roll(deg)');
legend('des','fb');
title('roll');
xlim([0 N*0.005])

%pitch
figure(2);
plot(t, pitch(1:N,1),'.-');
hold on;grid on;
plot(t, pitch(1:N,2),'.-');
xlabel('t/s');
ylabel('pitch(deg)');
legend('des','fb');
title('pitch');
xlim([0 N*0.005])

%yaw
figure(3);
plot(t, yaw(1:N,1),'.-');
hold on;grid on;
plot(t, yaw(1:N,2),'.-');
xlabel('t/s');
ylabel('yaw(deg)');
legend('des','fb');
title('yaw');
xlim([0 N*0.005])

figure;
[ax,h1,h2] = plotyy(t, Z_star(1,:), t, Z_star(2,:))
hold on;grid on;
set(h1,'color','b')
set(h2,'color','r')
set(ax(1),'xlim',[0,N*0.005]);
set(ax(2),'xlim',[0,N*0.005]);
h3 = plot(t, Z_star(3,:),'y')
hold on;
h4 = plot(t, Z_star(4,:),'c')
hold on;
xlabel('t/s');
ylabel('Zstar');
legend([h1 h2 h3 h4], 'q1','q2','q3','q4');
%legend('q1','q2','q3','q4');
title('star');
legend()
xlim([0 N*0.005])

figure;
plot(t, Z_gyro(1,:),'b')
hold on;grid on;
plot(t, Z_gyro(2,:),'r')
hold on;
plot(t, Z_gyro(3,:),'y')
hold on;
xlabel('t/s');
ylabel('Zgyro(rad/s)');
legend('phi','theta','psi');
title('gyro');
legend()
xlim([0 N*0.005])


