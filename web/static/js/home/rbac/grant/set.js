;
var grant_set_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        $(".grant_set_wrap .save").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }

            var level1_name_target = $(".grant_set_wrap input[name=level1_name]");
            var level1_name = level1_name_target.val();

            var level2_name_target = $(".grant_set_wrap input[name=level2_name]");
            var level2_name = level2_name_target.val();

            var name_target = $(".grant_set_wrap input[name=name]");
            var name = name_target.val();

            var url_target = $(".grant_set_wrap textarea[name=url]");
            var url = url_target.val();

            if( !common_ops.validate.length( level1_name,1,10 )) {
                common_ops.tip("请输入符合规范的一级菜单名称~~", level1_name_target);
                return;
            }

            if( !common_ops.validate.length( level2_name,1,10 )) {
                common_ops.tip("请输入符合规范的二级菜单名称~~", level2_name_target);
                return;
            }

            if( !common_ops.validate.length( name,1,10 )) {
                common_ops.tip("请输入符合规范的权限名称~~", name_target);
                return;
            }

            if( !common_ops.validate.length( url,1 )) {
                common_ops.tip("请输入符合规范的URL~~", url_target);
                return;
            }


            var data = $(".grant_set_wrap form").serialize();
            btn_target.addClass("disabled");

            $.ajax({
                url: home_common_ops.buildUrl('/rbac/grant/set'),
                data: data,
                type: 'POST',
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = {};
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = window.location.href;
                        }
                    }
                    common_ops.msg(res.msg, res.code == 200, callback);
                }
            });
        });

    }
};

$(document).ready(function () {
    grant_set_ops.init();
});
