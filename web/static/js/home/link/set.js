;
var link_set_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        $(".link_set_wrap .save").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }

            var type_target = $(".link_set_wrap select[name=type]");
            var type = type_target.val();

            var title_target = $(".link_set_wrap input[name=title]");
            var title = title_target.val();

            var url_target = $(".link_set_wrap input[name=url]");
            var url = url_target.val();


            if( type < 1  ){
                common_ops.tip("请选择分类~~", type_target);
                return;
            }

            if( !common_ops.validate.length( title,1,30 )) {
                common_ops.tip("请输入符合规范的标题~~", title_target);
                return;
            }
            if( !common_ops.validate.url(url )) {
                common_ops.tip("请输入符合规范的网址~~", url_target);
                return;
            }

            var data = $(".link_set_wrap form").serialize();
            btn_target.addClass("disabled");

            $.ajax({
                url: home_common_ops.buildUrl('/link/set'),
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
    link_set_ops.init();
});
