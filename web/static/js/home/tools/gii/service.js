;
var gii_service_ops = {
    init: function () {
        this.eventBind();
        this.previewPath();
    },
    eventBind: function () {
        var that = this;


        $(".gii_service_wrap input[name=filename]").change(function () {
            that.previewPath();
        });

        $(".gii_service_wrap input[name=path]").bind("input",function(){
            that.previewPath();
        });

        $(".gii_service_wrap .save").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }

            var filename_target = $(".gii_service_wrap input[name=filename]");
            var filename = filename_target.val();


            if (!common_ops.validate.length(filename, 1, 30)) {
                common_ops.tip("请输入文件名，例如monitor~~", filename_target);
                return;
            }

            var data = $(".gii_service_wrap form").serialize();
            btn_target.addClass("disabled");

            $.ajax({
                url: home_common_ops.buildUrl('/tools/gii/service'),
                data: data,
                type: 'POST',
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = {};
                    if (res.code == 200) {
                        common_ops.msg(res.msg, res.code == 200, callback);
                    } else {
                        common_ops.alert(res.msg);
                    }

                }
            });
        });
    },
    previewPath: function () {
        var prefix_path = $(".gii_service_wrap .prefix_path").text();
        var path = $(".gii_service_wrap input[name=path]").val();
        var filename = $(".gii_service_wrap input[name=filename]").val();
        var model_path = prefix_path;
        if( path ){
            model_path += path + "/";
        }
        if (filename) {
            var reg = new RegExp( ' ' , "g" );
            filename = filename.replace(reg,"")
            model_path += filename.slice(0, 1).toUpperCase() + filename.slice(1) + "Service.py"
        }
        $(".gii_service_wrap .preview_path").html(model_path);
    }
};

$(document).ready(function () {
    gii_service_ops.init();
});