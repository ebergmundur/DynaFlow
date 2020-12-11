
const routes = [
  // {
  //   path: '/',
  //   component: () => import('src/App.vue')
  // },
  {
    path: '/',
    component: () => import('src/layouts/MainLayout'),
    children: [
      { path: '', name: 'home', component: () => import('pages/Index.vue') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/question',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('components/Question.vue') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/collect',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('components/CollectQuestions.vue') }
    ],
    meta: {
      requiresLogged: false
    }
  },

  {
    path: '/createtest',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('components/CreatePractice.vue') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/testreal',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('components/Testpage') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/testpractice',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'testpage', component: () => import('components/Testpage') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/review',
    props: { exam: 1 },
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'review', component: () => import('components/Review') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/flipcard',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'flipcard', component: () => import('components/Flipcard') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/dashboard',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'dashboard', component: () => import('components/Dashboard') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/userinfo',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'userinfo', component: () => import('components/User') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/login',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'login', component: () => import('components/Login') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/register',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'register', component: () => import('components/Register') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/logout',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'logout', component: () => import('components/Logout') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  // {
  //   path: '/callback',
  //   component: () => import('layouts/MainLayout.vue'),
  //   children: [
  //     { path: '', component: () => import('components/Clock') }
  //   ]
  // },
  // {
  //   path: '/callback',
  //   component: () => import('layouts/MainLayout.vue'),
  //   children: [
  //     { path: '', name: 'downloads', component: () => import('components/Dashboard') }
  //   ]
  // },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue'),
    meta: {
      requiresLogged: false
    }
  }
]

export default routes
