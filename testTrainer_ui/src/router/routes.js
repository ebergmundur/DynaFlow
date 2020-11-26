
const routes = [
  {
    path: '/',
    name: 'front',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
      // { path: '', component: () => import('components/Questions.vue') }
    ]
  },
  {
    path: '/question',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      // { path: '', component: () => import('components/Questions.vue') },
      { path: '', component: () => import('components/Question.vue') }
    ]
  },
  {
    path: '/collect',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      // { path: '', component: () => import('components/Questions.vue') },
      { path: '', component: () => import('components/CollectQuestions.vue') }
    ]
  },
  {
    path: '/createtest',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      // { path: '', component: () => import('components/Questions.vue') },
      { path: '', component: () => import('components/CreatePractice.vue') }
    ]
  },
  {
    path: '/testpage',
    name: 'testpage',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      // { path: '', component: () => import('components/Questions.vue') },
      { path: '', component: () => import('components/Testpage') }
    ]
  },
  {
    path: '/review',
    props: { exam: 1 },
    name: 'review',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      // { path: '', component: () => import('components/Questions.vue') },
      { path: '', component: () => import('components/Testpage') }
    ]
  },
  {
    path: '/dashboard',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      // { path: '', component: () => import('components/Questions.vue') },
      { path: '', component: () => import('components/Clock') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
