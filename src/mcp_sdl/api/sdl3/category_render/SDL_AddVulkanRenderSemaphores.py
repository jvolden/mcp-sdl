"""SDL_AddVulkanRenderSemaphores function definition."""

FUNCTION = {
    "SDL_AddVulkanRenderSemaphores": {
        "category": "render",
        "description": "Add Vulkan semaphores for synchronizing rendering with external Vulkan operations",
        "signature": "bool SDL_AddVulkanRenderSemaphores(SDL_Renderer *renderer, Uint32 wait_stage_mask, Sint64 wait_semaphore, Sint64 signal_semaphore)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "wait_stage_mask", "type": "Uint32", "description": "VkPipelineStageFlags for when to wait"},
            {"name": "wait_semaphore", "type": "Sint64", "description": "VkSemaphore to wait on before rendering"},
            {"name": "signal_semaphore", "type": "Sint64", "description": "VkSemaphore to signal after rendering"}
        ],
        "returns": "true on success or false on failure",
        "example": """if (SDL_AddVulkanRenderSemaphores(renderer, VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT, wait_sem, signal_sem)) {
    SDL_Log("Vulkan semaphores added");
}""",
        "remarks": "[Vulkan only] Enables synchronization between SDL and custom Vulkan code",
        "see_also": ["SDL_CreateRenderer"]
    }
}
