document.addEventListener('DOMContentLoaded', function() {
    const btnMenu = document.querySelectorAll('.btn-menu');
    const navLateral = document.querySelector('.navLateral');
    const navLateralBg = document.querySelector('.navLateral-bg');
    const btnShowNotifications = document.querySelector('.btn-show-notifications');
    const containerNotifications = document.querySelector('.container-notifications-bg');
    const notificationArea = document.querySelector('.NotificationArea');

    btnMenu.forEach(function(btn) {
        btn.addEventListener('click', function() {
            if (navLateral.style.left === '0px') {
                navLateral.style.left = '-250px';
                navLateralBg.style.display = 'none';
            } else {
                navLateral.style.left = '0';
                navLateralBg.style.display = 'block';
            }
        });
    });

    navLateralBg.addEventListener('click', function() {
        navLateral.style.left = '-250px';
        navLateralBg.style.display = 'none';
    });

    btnShowNotifications.addEventListener('click', function() {
        if (notificationArea.style.display === 'block') {
            closeNotifications();
        } else {
            openNotifications();
        }
    });
    

    function openNotifications() {
        notificationArea.style.display = 'block';
        containerNotifications.style.display = 'block';
    }

    function closeNotifications() {
        notificationArea.style.display = 'none';
        containerNotifications.style.display = 'none';
    }
});