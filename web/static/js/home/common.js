;
var home_common_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        this.setMenuIconHighLight();
        this.newsPop();
    },
    setMenuIconHighLight: function () {

       if ($(".main-sidebar .sidebar-menu li.treeview").length < 1) {
            return;
        }

        var pathname = window.location.pathname;

        var nav_name = "dashboard";

        if( pathname.indexOf("/link/") > -1 ){
            nav_name = "link";
        }

        if( pathname.indexOf("/rbac/") > -1 ){
            nav_name = "rbac";
        }

        if( pathname.indexOf("/log/") > -1 ){
            nav_name = "log";
        }

        if( pathname.indexOf("/tools/") > -1 ){
            nav_name = "tools";
        }


        if (nav_name == null) {
            return;
        }

        $(".main-sidebar .sidebar-menu li.menu_" + nav_name).addClass("active");

        //继续高亮子菜单
        $(".sidebar-menu .treeview-menu li a").each(function () {
            var link_url = $(this).attr("href");
            if (link_url.indexOf(pathname) > -1) {
                $(this).parent("li").addClass("active");
                return false;
            }
        });
    },
    buildUrl: function (path, params) {
        var url = $(".hidden_val_wrap input[name=domain]").val() + path;
        var _paramUrl = "";
        if(  params ){
            _paramUrl = Object.keys( params ).map( function( k ){
                return [ encodeURIComponent( k ),encodeURIComponent( params[ k ] ) ].join("=");
            }).join("&");
            _paramUrl = "?" + _paramUrl;
        }
        return url + _paramUrl;
    },
    newsPop:function(){
        if( $(".main-header .notifications-menu").length < 1 ){
            return;
        }
        var that = this;
        $.ajax({
            url: this.buildUrl("/news"),
            dataType: "json",
            success: function (res) {
                if (res.code != 200 ) {
                    return;
                }

                $(".main-header .notifications-menu").html( res.data.content );
                $('[data-toggle="tooltip"]').tooltip({ "html":true });
                $("body").on('click','.main-header .notifications-menu [data-stop-propagation]',function (e) {
                    that.updateNews($(this).attr( "data-id" ) );
                    $(this).parent("li").remove();
                    e.stopPropagation();
                });
            }
        });
    },
    updateNews: function (id) {
        $.ajax({
            url: this.buildUrl("/profile/news/ops"),
            type: "POST",
            data: {
                id: id
            },
            dataType: "json",
            success: function (res) {
            }
        });
    },
};
var common_ops_url = {
    buildUrl:function( path, params ){
        return home_common_ops.buildUrl( path, params );
    }
};

$(document).ready(function () {
    home_common_ops.init();
    $('[data-toggle="tooltip"]').tooltip();
});