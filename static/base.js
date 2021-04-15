const $menu = $('#navbarToggleExternalContent');

$menu.on('show.bs.collapse', function () {
    $menu.addClass('menu-show');
});

$menu.on('hide.bs.collapse', function () {
    $menu.removeClass('menu-show');
});