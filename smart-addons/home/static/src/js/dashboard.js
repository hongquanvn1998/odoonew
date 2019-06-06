odoo.define('home.Dashboard', function (require) {
    var core = require('web.core');
    var session = require('web.session');
    var Widget = require('web.Widget');

    var rpc = require('web.rpc');
    var id = session.uid; 
    $(function () {
       // setTimeout(LoadMenu,1000); 
       LoadMenu()
    }); 

    function LoadMenu() {
        rpc.query({
            model: 'ir.ui.menu',
            method: 'load_menus',
            args: [false],
            kwargs: {
                context: {
                    lang: "en_US",
                    tz: false,
                    uid: id
                }
            }
        }).then(function (res) {
            
            var _itemHtml ="";
            res.children.forEach(item => {
                console.log(item.action)
                let actionId = item.action?item.action.split(',')[1]:0|| 0

             _itemHtml +=   `
             <div class="col-xs-3 mx-auto px-3 py-3">
             <div>
             <a class="home-menu-icon" role="menuitem" 
              data-action-id="${actionId}"
              data-menu-id="${item.id}" 
              data-menu-xmlid="${item.xmlid}" 
              href="#menu_id=${item.id}&amp;action_id=${actionId}">
                    
            
        <img class="o-app-icon" src="/web/image/ir.ui.menu/${item.id}/web_icon_data">
           </div>
           <div class="mt-3">
        <span class="o-app-name-sml py-3">
            ${item.name}
        </span> 
        </div>
        </a></div>`
            }); 
            $("#home-menu").html(_itemHtml)
        });
    }
});