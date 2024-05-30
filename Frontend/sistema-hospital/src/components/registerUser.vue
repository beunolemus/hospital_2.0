<template> 
    <section class="bg-gray-100 min-h-screen flex box-border justify-center items-center"> 
        <div class="bg-[#dfa674] rounded-2xl flex max-w-3xl p-5 items-center"> 
            <div class="md:w-1/2 px-8"> 
                <h2 class="font-bold text-3xl text-[#002D74]">Registro</h2> 
                <p class="text-sm mt-4 text-[#002D74]">Crea una cuenta para acceder.</p> 
 
                <form action="" class="flex flex-col gap-4"> 
                    <input class="p-2 mt-8 rounded-xl border" type="text" name="name" placeholder="Nombre"> 
                    <input class="p-2 rounded-xl border" type="email" name="email" placeholder="Email"> 
                    <div class="relative"> 
                        <input class="p-2 rounded-xl border w-full" type="password" name="password" id="password" placeholder="Contraseña"> 
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="gray" id="togglePassword" 
                            class="bi bi-eye absolute top-1/2 right-3 -translate-y-1/2 cursor-pointer z-20 opacity-100" 
                            viewBox="0 0 16 16"> 
                            <!-- Icono del ojo para mostrar contraseña --> 
                        </svg> 
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" 
                            class="bi bi-eye-slash-fill absolute top-1/2 right-3 -z-1 -translate-y-1/2 cursor-pointer hidden" 
                            id="mama" viewBox="0 0 16 16"> 
                            <!-- Icono del ojo tachado para ocultar contraseña --> 
                        </svg> 
                    </div> 
                    <button class="bg-[#002D74] text-white py-2 rounded-xl hover:scale-105 duration-300 hover:bg-[#206ab1] font-medium" type="submit">Registrarse</button> 
                </form> 
                <div class="mt-6 items-center text-gray-100"> 
                    <hr class="border-gray-300"> 
                    <p class="text-center text-sm">O</p> 
                    <hr class="border-gray-300"> 
                </div> 
 
                <div class="mt-10 text-sm border-b border-gray-500 py-5 playfair tooltip">¿Olvidaste tu contraseña?</div> 
 
                <div class="mt-4 text-sm flex justify-between items-center container-mr"> 
                    <p class="mr-3 md:mr-0 ">¿Ya tienes una cuenta?</p> 
                    <RouterLink to="/"> 
                        <button class="hover:border register text-white bg-[#002D74] hover:border-gray-400 rounded-xl py-2 px-5 hover:scale-110 hover:bg-[#002c7424] font-semibold duration-300">Iniciar Sesión</button> 
                    </RouterLink> 
                </div> 
            </div> 
        </div> 
    </section> 
</template> 
