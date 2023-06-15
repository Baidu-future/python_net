import { S as SvelteComponent, y as init$1, z as safe_not_equal, an as append_styles, E as create_component, G as mount_component, aC as noop, M as transition_in, K as transition_out, O as destroy_component } from '../profile-b0e03603.js';
import { y as yb } from '../App-507b3fa6.js';

function l(t){append_styles(t,"svelte-1qxpon2","body{height:100%;width:100%}:root{--app-content-width:calc(100% - 40px);--top-bar-width:calc(100% - 35px);--profiles-list-min-height:inherit}");}function m(t){let s,a;return s=new yb({}),{c(){create_component(s.$$.fragment);},m(t,e){mount_component(s,t,e),a=!0;},p:noop,i(t){a||(transition_in(s.$$.fragment,t),a=!0);},o(t){transition_out(s.$$.fragment,t),a=!1;},d(t){destroy_component(s,t);}}}const d=new class extends SvelteComponent{constructor(t){super(),init$1(this,t,null,m,safe_not_equal,{},l);}}({target:document.body});

export default d;
