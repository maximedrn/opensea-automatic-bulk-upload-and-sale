// app/services/solvers/recaptcha.py


/*
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
*/


function recaptchaCallback() {

    if (typeof (___grecaptcha_cfg) !== "undefined") {
        return Object.entries(___grecaptcha_cfg.clients).map(([cid, client]) => {
            var callback = "";
            const objects = Object.entries(client).filter(([_, value]) => value && typeof value === "object");

            objects.forEach(([toplevelKey, toplevel]) => {
                const found = Object.entries(toplevel).find(([_, value]) => (
                    value && typeof value === "object" && "sitekey" in value && "size" in value
                ));
                        
                if (found) {
                    const [sublevelKey, sublevel] = found;
                    const callbackKey = cid >= 10000 ? "V3" : "V2" === "V2" ? "callback" : "promise-callback";

                    if (sublevel[callbackKey]) {
                        callback = `___grecaptcha_cfg.clients["${cid}"].${toplevelKey}.${sublevelKey}.${callbackKey}`;	
                    }
                }
            });

            return callback;
        })[0];
    }

    return "";
}
