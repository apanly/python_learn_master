;
var common_ops = {
    init:function(){
       this.eventBind();
    },
    eventBind:function(){

    },
    alert:function( msg ,cb ){
        layer.alert( msg,{
            yes:function( index ){
                if( typeof cb == "function" ){
                    cb();
                }
                layer.close( index );
            }
        });
    },
    confirm:function( msg,callback ){
        callback = ( callback != undefined )?callback: { 'ok':null, 'cancel':null };
        layer.confirm( msg , {
            btn: ['确定','取消'] //按钮
        }, function( index ){
            //确定事件
            if( typeof callback.ok == "function" ){
                callback.ok();
            }
            layer.close( index );
        }, function( index ){
            //取消事件
            if( typeof callback.cancel == "function" ){
                callback.cancel();
            }
            layer.close( index );
        });
    },
    tip:function( msg,target ){
        layer.tips( msg, target, {
            tips: [ 3, '#e5004f']
        });
        $('html, body').animate({
            scrollTop: target.offset().top - 10
        }, 100);
    },
    msg:function( msg,flag,callback ){
        callback = (callback != undefined && typeof callback == "function") ? callback : null;
        var params = {
            "icon":6,
            "time": 1000,
            "shade" :[0.5 , '#000' , true]
        };
        if( !flag ){
            params['icon'] = 5;
            params['time'] = 1500;
        }
        layer.msg( msg ,params,callback );
    },
    validate:{
        email:function( param ){
            if( param == undefined ){
                return false;
            }
            return /^\w+((.\w+)|(-\w+))@[A-Za-z0-9]+((.|-)[A-Za-z0-9]+).[A-Za-z0-9]+$/.test( param );
        },
        length:function( param,min,max ){
            min = min || 1;
            max = max || null;
            if( param == undefined ) {
                return false;
            }

            if( param.length < min ){
                return false;
            }

            if( max != null && param.length > max){
                return false;
            }
            return true;
        },
        mobile:function( param ){
            if( param == undefined ){
                return false;
            }
            var match = /^1[0-9]{10}$/;
            return match.test( param );
        },
        date:function ( date ) {
            return /^\d{4}-\d{2}-\d{2}$/.test( date );
        },
        url:function( url ){
            return /http(s)?:\/\/([\w-]+\.)+[\w-]+(\/[\w- .\/?%&=]*)?/.test( url );
        }
    },
    getQueryString:function( name ){
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
        var r = window.location.search.substr(1).match(reg);
        if (r != null) return unescape(r[2]);
        return null;
    },
    popLayer:function( url,data,modal_params){
        if( modal_params == undefined ){
            modal_params = {};
        }

        if( !modal_params.hasOwnProperty("backdrop") ){
            modal_params['backdrop'] = false;
        }
        $.ajax({
            url: url,
            data: data,
            type: "GET",
            dataType: 'json',
            success: function (res) {
                if(res.code != 200 ){
                    common_ops.alert(res.msg);
                    return;
                }
                $("#pop_layer").html( res.data.content );
                $('#pop_layer').modal( modal_params );
            }
        });
    },
    errorHandler:function( data ){
        console.log( data );
    }
};

$(document).ready(function () {
    common_ops.init();
});
/**
 * 正式代码如果有console.log
 * 提交到错误平台
 * **/
window.onerror = function (message, url, lineNumber, columnNo, error) {
    var data = {
        'message': message,
        'url': url,
        'error': error?error.stack:""
    };
    common_ops.errorHandler( data );
    return true;
};
